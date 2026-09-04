# Mallverse Admin

Interface Angular 17 para a API Mallverse. As rotas da interface são:

| Rota | Recurso |
| --- | --- |
| `/shoppings` | shoppings e cidades |
| `/lojas` | lojas vinculadas a shoppings |
| `/funcionarios` | funcionários vinculados a lojas |
| `/clientes` | clientes |
| `/estacionamento` | setores e capacidade de vagas |
| `/avaliacoes` | avaliações vinculadas a clientes |
| `/contratos` | contratos vinculados a loja e shopping |

## Executar

Em um terminal, inicie a API na raiz do projeto:

```bash
uvicorn src.app:app --reload
```

Em outro, inicie o frontend:

```bash
cd frontend
npm install
npm start
```

Abra `http://localhost:4200`. Não abra `src/index.html` diretamente nem use Live Server na pasta `src`: esse arquivo é apenas o template que o Angular CLI compila e, isolado, exibe somente o fundo da página e a tag vazia `<app-root>`.

Para publicar a versão estática, execute `npm run build` e sirva os arquivos em `dist/mallverse-admin/browser/` por um servidor HTTP. O cliente usa `http://localhost:8000/api`; a API foi configurada para expor esse prefixo e aceitar a origem do Angular.

Cada tela oferece busca local, paginação, criação, edição e exclusão. Campos relacionais são selecionados a partir dos dados atuais da API e os erros HTTP são mostrados na tela.
