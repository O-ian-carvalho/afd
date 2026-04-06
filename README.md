
---

# Como declarar o AFD no JSON

Você precisa criar um arquivo `afd.json` com 5 partes principais:

```json
{
  "states": ["q0", "q1"],
  "alphabet": ["0", "1"],
  "start_state": "q0",
  "end_states": ["q1"],
  "transitions": {
    "q0": { "0": "q1", "1": "q0" },
    "q1": { "0": "q1", "1": "q0" }
  }
}
```

---

##  O que cada parte significa

* **states** → todos os estados do autômato

  ```json
  ["q0", "q1"]
  ```

* **alphabet** → símbolos permitidos

  ```json
  ["0", "1"]
  ```

* **start_state** → estado inicial

  ```json
  "q0"
  ```

* **end_states** → estados de aceitação

  ```json
  ["q1"]
  ```

* **transitions** → regras de transição

  ```json
  "q0": { "0": "q1", "1": "q0" }
  ```

   Significa:

  * de `q0` com `0` vai para `q1`
  * de `q0` com `1` vai para `q0`


Se quiser, posso montar um AFD específico pra você (tipo: aceitar números pares, strings com final “01”, etc.) 👍
