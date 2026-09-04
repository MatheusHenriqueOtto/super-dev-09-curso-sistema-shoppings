import { Routes } from '@angular/router';
import { ManagementComponent } from './management.component';
export const routes: Routes = [
  { path: ':resource', component: ManagementComponent },
  { path: '', pathMatch: 'full', redirectTo: 'shoppings' },
  { path: '**', redirectTo: 'shoppings' }
];
