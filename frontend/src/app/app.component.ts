import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({ selector: 'app-root', standalone: true, imports: [RouterOutlet, RouterLink, RouterLinkActive], template: `
  <div class="shell"><aside><a class="brand" routerLink="/shoppings"><span>◆</span> MALLVERSE <small>ADMIN</small></a><nav aria-label="Navegação principal">
    @for (item of nav; track item.path) { <a [routerLink]="['/', item.path]" routerLinkActive="active"><i>{{item.icon}}</i>{{item.label}}</a> }
  </nav><div class="side-foot">Sistema de gestão<br><strong>Rede de shoppings</strong></div></aside>
  <main><header><div><p>OPERAÇÕES</p><h1>Central de administração</h1></div><div class="online"><b></b> API conectada</div></header><router-outlet /></main></div>` })
export class AppComponent {
  readonly nav = [
    { path: 'shoppings', label: 'Shoppings', icon: '◈' }, { path: 'lojas', label: 'Lojas', icon: '▣' },
    { path: 'funcionarios', label: 'Funcionários', icon: '♙' }, { path: 'clientes', label: 'Clientes', icon: '◎' },
    { path: 'estacionamento', label: 'Estacionamento', icon: 'P' }, { path: 'avaliacoes', label: 'Avaliações', icon: '★' }, { path: 'contratos', label: 'Contratos', icon: '▤' }
  ];
}
