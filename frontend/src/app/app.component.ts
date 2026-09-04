import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({ selector: 'app-root', standalone: true, imports: [RouterOutlet, RouterLink, RouterLinkActive], template: `
  <div class="shell"><aside><a class="brand" routerLink="/shoppings"><span class="material-symbols-rounded">diamond</span> MALLVERSE <small>ADMIN</small></a><nav aria-label="Navegação principal">
    @for (item of nav; track item.path) { <a [routerLink]="['/', item.path]" routerLinkActive="active"><i class="material-symbols-rounded">{{item.icon}}</i>{{item.label}}</a> }
  </nav><div class="side-foot">Sistema de gestão<br><strong>Rede de shoppings</strong></div></aside>
  <main><header><div><p>OPERAÇÕES</p><h1>Central de administração</h1></div><div class="online"><b></b> API conectada</div></header><router-outlet /></main></div>` })
export class AppComponent {
  readonly nav = [
    { path: 'shoppings', label: 'Shoppings', icon: 'storefront' }, { path: 'lojas', label: 'Lojas', icon: 'store' },
    { path: 'funcionarios', label: 'Funcionários', icon: 'badge' }, { path: 'clientes', label: 'Clientes', icon: 'groups' },
    { path: 'estacionamento', label: 'Estacionamento', icon: 'local_parking' }, { path: 'avaliacoes', label: 'Avaliações', icon: 'star' }, { path: 'contratos', label: 'Contratos', icon: 'description' }
  ];
}
