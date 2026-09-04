import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Entity } from '../../models/entities.model';

/** Centraliza o contrato REST do Mallverse. */
@Injectable({ providedIn: 'root' })
export class ApiService {
  private readonly baseUrl = 'http://localhost:8000/api';
  constructor(private readonly http: HttpClient) {}
  list<T extends Entity>(resource: string): Observable<T[]> { return this.http.get<T[]>(`${this.baseUrl}/${resource}`); }
  create<T extends Entity>(resource: string, value: Partial<T>): Observable<T> { return this.http.post<T>(`${this.baseUrl}/${resource}`, value); }
  update<T extends Entity>(resource: string, id: number, value: Partial<T>): Observable<unknown> { return this.http.put(`${this.baseUrl}/${resource}/${id}`, value); }
  delete(resource: string, id: number): Observable<unknown> { return this.http.delete(`${this.baseUrl}/${resource}/${id}`); }
}
