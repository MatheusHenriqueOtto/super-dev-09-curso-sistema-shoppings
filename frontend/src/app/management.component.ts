import { Component, OnDestroy, OnInit } from '@angular/core';
import { CommonModule, CurrencyPipe, DatePipe } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { FormBuilder, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { Subscription, forkJoin } from 'rxjs';
import { ApiService } from './core/services/api.service';
import { Entity } from './models/entities.model';

type FieldKind = 'text' | 'number' | 'date' | 'textarea' | 'select';
interface Field { key: string; label: string; type: FieldKind; required?: boolean; ref?: 'shoppings' | 'lojas' | 'clientes'; }
interface Config { title: string; singular: string; resource: string; fields: Field[]; }

const CONFIGS: Record<string, Config> = {
  shoppings: { title: 'Shoppings', singular: 'shopping', resource: 'shoppings', fields: [{key:'nome',label:'Nome',type:'text',required:true},{key:'cnpj',label:'CNPJ',type:'text',required:true},{key:'cidade',label:'Cidade',type:'text',required:true}] },
  lojas: { title: 'Lojas', singular: 'loja', resource: 'lojas', fields: [{key:'nome_fantasia',label:'Nome fantasia',type:'text',required:true},{key:'numero_modulo',label:'Módulo',type:'text',required:true},{key:'id_shopping',label:'Shopping',type:'select',ref:'shoppings',required:true}] },
  funcionarios: { title: 'Funcionários', singular: 'funcionário', resource: 'funcionarios', fields: [{key:'nome',label:'Nome',type:'text',required:true},{key:'cpf',label:'CPF',type:'text',required:true},{key:'cargo',label:'Cargo',type:'text',required:true},{key:'id_loja',label:'Loja',type:'select',ref:'lojas',required:true}] },
  clientes: { title: 'Clientes', singular: 'cliente', resource: 'clientes', fields: [{key:'nome',label:'Nome',type:'text',required:true},{key:'cpf',label:'CPF',type:'text',required:true},{key:'telefone',label:'Telefone',type:'text'}] },
  estacionamento: { title: 'Estacionamento', singular: 'área de estacionamento', resource: 'estacionamento', fields: [{key:'setor',label:'Setor',type:'text',required:true},{key:'capacidade_vagas',label:'Capacidade de vagas',type:'number',required:true},{key:'id_shopping',label:'Shopping',type:'select',ref:'shoppings'}] },
  avaliacoes: { title: 'Avaliações', singular: 'avaliação', resource: 'avaliacoes', fields: [{key:'nota',label:'Nota (1 a 5)',type:'number',required:true},{key:'id_cliente',label:'Cliente',type:'select',ref:'clientes',required:true},{key:'comentario',label:'Comentário',type:'textarea'}] },
  contratos: { title: 'Contratos', singular: 'contrato', resource: 'contratos', fields: [{key:'id_loja',label:'Loja',type:'select',ref:'lojas',required:true},{key:'id_shopping',label:'Shopping',type:'select',ref:'shoppings',required:true},{key:'data_inicio',label:'Início',type:'date',required:true},{key:'data_fim',label:'Fim',type:'date',required:true},{key:'valor_aluguel',label:'Aluguel mensal',type:'number',required:true}] }
};

@Component({ selector: 'app-management', standalone: true, imports: [CommonModule, RouterLink, FormsModule, ReactiveFormsModule, CurrencyPipe, DatePipe], template: `
<section class="page">
  <div class="page-title"><div><h2>{{config.title}}</h2><p>Gerencie os registros da rede Mallverse.</p></div><button class="primary" (click)="openCreate()">+ Novo {{config.singular}}</button></div>
  <div class="metrics"><article><span>REGISTROS ATIVOS</span><strong>{{items.length}}</strong></article><article><span>EXIBIDOS</span><strong>{{filtered.length}}</strong></article><article><span>STATUS</span><strong class="good">Operacional</strong></article></div>
  <div class="panel"><div class="toolbar"><label class="search">⌕ <input aria-label="Filtrar registros" [(ngModel)]="query" (ngModelChange)="page=1" placeholder="Buscar em {{config.title.toLowerCase()}}..."></label><button class="ghost" (click)="load()">↻ Atualizar</button></div>
    @if (loading) { <div class="state">Carregando dados...</div> } @else if (filtered.length === 0) { <div class="state">Nenhum registro encontrado.</div> } @else { <div class="table-wrap"><table><thead><tr>@for(field of config.fields; track field.key){<th>{{field.label}}</th>}<th>Status</th><th aria-label="Ações"></th></tr></thead><tbody>
      @for (item of paged; track item.id) {<tr>@for(field of config.fields; track field.key){<td>{{display(item, field)}}</td>}<td><span class="badge">Ativo</span></td><td class="actions"><button (click)="edit(item)" [attr.aria-label]="'Editar '+item.id">Editar</button><button class="delete" (click)="remove(item)">Excluir</button></td></tr>}
    </tbody></table></div><footer><span>Mostrando {{paged.length}} de {{filtered.length}} registros</span><div><button class="ghost" [disabled]="page===1" (click)="page=page-1">Anterior</button><span>{{page}} / {{pages}}</span><button class="ghost" [disabled]="page===pages" (click)="page=page+1">Próxima</button></div></footer> }
  </div>
</section>
@if (editing) {<div class="overlay" (click)="close()"><section class="modal" role="dialog" aria-modal="true" [attr.aria-label]="editing.id ? 'Editar registro' : 'Criar registro'" (click)="$event.stopPropagation()"><header><div><p>{{editing.id ? 'EDIÇÃO' : 'NOVO REGISTRO'}}</p><h2>{{editing.id ? 'Editar' : 'Cadastrar'}} {{config.singular}}</h2></div><button class="close" (click)="close()" aria-label="Fechar">×</button></header><form [formGroup]="form" (ngSubmit)="save()"><div class="form-grid">@for(field of config.fields; track field.key){<label [class.wide]="field.type === 'textarea'"><span>{{field.label}} @if(field.required){<b>*</b>}</span>@switch(field.type){@case('textarea'){<textarea [formControlName]="field.key" rows="3"></textarea>}@case('select'){<select [formControlName]="field.key"><option [ngValue]="null">Selecione...</option>@for(ref of refs[field.ref!];track ref.id){<option [ngValue]="ref.id">{{labelFor(ref, field.ref!)}}</option>}</select>}@default{<input [type]="field.type" [formControlName]="field.key">}}</label>}</div><p class="form-error" *ngIf="submitted && form.invalid">Preencha os campos obrigatórios.</p><div class="form-actions"><button type="button" class="ghost" (click)="close()">Cancelar</button><button type="submit" class="primary" [disabled]="saving">{{saving ? 'Salvando...' : 'Salvar alterações'}}</button></div></form></section></div>}
@if (notice) {<div class="toast" [class.error]="notice.error">{{notice.text}}</div>}
` })
export class ManagementComponent implements OnInit, OnDestroy {
  config: Config = CONFIGS['shoppings']; items: Entity[] = []; refs: Record<string, Entity[]> = { shoppings: [], lojas: [], clientes: [] };
  query = ''; page = 1; readonly limit = 8; loading = false; saving = false; submitted = false; editing?: Entity; notice?: {text:string; error:boolean}; private sub = new Subscription();
  form = this.fb.group({});
  constructor(private readonly route: ActivatedRoute, private readonly api: ApiService, private readonly fb: FormBuilder) {}
  ngOnInit(): void { this.sub.add(this.route.paramMap.subscribe(params => { this.config = CONFIGS[params.get('resource') ?? 'shoppings'] ?? CONFIGS['shoppings']; this.makeForm(); this.load(); })); }
  ngOnDestroy(): void { this.sub.unsubscribe(); }
  get filtered(): Entity[] { const term = this.query.trim().toLocaleLowerCase(); return !term ? this.items : this.items.filter(x => this.config.fields.some(f => this.display(x, f).toLocaleLowerCase().includes(term))); }
  get pages(): number { return Math.max(1, Math.ceil(this.filtered.length / this.limit)); }
  get paged(): Entity[] { if (this.page > this.pages) this.page = this.pages; return this.filtered.slice((this.page - 1) * this.limit, this.page * this.limit); }
  makeForm(): void { const controls: Record<string, any> = {}; for (const f of this.config.fields) controls[f.key] = [null, f.required ? Validators.required : []]; this.form = this.fb.group(controls); }
  load(): void { this.loading = true; this.sub.add(forkJoin({ items: this.api.list<Entity>(this.config.resource), shoppings: this.api.list<Entity>('shoppings'), lojas: this.api.list<Entity>('lojas'), clientes: this.api.list<Entity>('clientes') }).subscribe({ next: result => { this.items = result.items; this.refs = {shoppings:result.shoppings, lojas:result.lojas, clientes:result.clientes}; this.loading=false; }, error: e => {this.loading=false; this.flash(this.message(e), true);} })); }
  openCreate(): void { this.editing = {} as Entity; this.submitted = false; this.form.reset(); }
  edit(item: Entity): void { this.editing = item; this.submitted=false; const values: Record<string, unknown> = {}; this.config.fields.forEach(f => values[f.key] = item[f.key] ?? null); this.form.reset(values); }
  close(): void { this.editing = undefined; this.submitted=false; }
  save(): void { this.submitted=true; if(this.form.invalid || !this.editing) return; this.saving=true; const payload = this.normalized(); const request = this.editing.id ? this.api.update(this.config.resource, this.editing.id, payload) : this.api.create(this.config.resource, payload); this.sub.add(request.subscribe({next:()=>{this.saving=false;this.close();this.flash('Registro salvo com sucesso.',false);this.load();},error:e=>{this.saving=false;this.flash(this.message(e),true)}})); }
  remove(item: Entity): void { if (!confirm(`Excluir este ${this.config.singular}? Esta ação não pode ser desfeita.`)) return; this.sub.add(this.api.delete(this.config.resource,item.id).subscribe({next:()=>{this.flash('Registro excluído com sucesso.',false);this.load();},error:e=>this.flash(this.message(e),true)})); }
  normalized(): Partial<Entity> { const value = this.form.getRawValue() as Record<string, unknown>; this.config.fields.forEach(f => { if (f.type === 'number' && value[f.key] !== null) value[f.key] = Number(value[f.key]); if (f.type === 'select' && value[f.key] !== null) value[f.key] = Number(value[f.key]); }); return value as Partial<Entity>; }
  display(item: Entity, field: Field): string { const value = item[field.key]; if(value === null || value === undefined || value === '') return '—'; if(field.ref) return this.labelFor(this.refs[field.ref]?.find(x=>x.id === value),field.ref); if(field.key === 'valor_aluguel') return new Intl.NumberFormat('pt-BR',{style:'currency',currency:'BRL'}).format(Number(value)); if(field.type === 'date') return new Date(`${value}T00:00:00`).toLocaleDateString('pt-BR'); return String(value); }
  labelFor(item: Entity | undefined, ref: string): string { if(!item) return 'Não encontrado'; return ref === 'lojas' ? String(item['nome_fantasia']) : String(item['nome']); }
  flash(text:string,error:boolean):void {this.notice={text,error}; setTimeout(()=>this.notice=undefined,4000);}
  message(error: any): string { return error?.error?.detail ?? 'Não foi possível concluir a operação. Confira se a API está disponível.'; }
}
