nodos={
  "estados": [
    "q0",
    "q1",
    "q2"
  ],
  "transiciones": [
    {
      "inicio": "q0",
      "fin": "q0",
      "cadena": "b",
      "buscar": "b",
      "insertar": "bb"
    },
    {
      "inicio": "q0",
      "fin": "q0",
      "cadena": "a",
      "buscar": "b",
      "insertar": "ba"
    },
    {
      "inicio": "q0",
      "fin": "q0",
      "cadena": "b",
      "buscar": "a",
      "insertar": "ab"
    },
    {
      "inicio": "q0",
      "fin": "q0",
      "cadena": "a",
      "buscar": "a",
      "insertar": "aa"
    },
    {
      "inicio": "q0",
      "fin": "q0",
      "cadena": "b",
      "buscar": "#",
      "insertar": "#b"
    },
    {
      "inicio": "q0",
      "fin": "q0",
      "cadena": "a",
      "buscar": "#",
      "insertar": "#a"
    },
    {
      "inicio": "q0",
      "fin": "q1",
      "cadena": "c",
      "buscar": "#",
      "insertar": "#"
    },
    {
      "inicio": "q0",
      "fin": "q1",
      "cadena": "c",
      "buscar": "b",
      "insertar": "b"
    },
    {
      "inicio": "q0",
      "fin": "q1",
      "cadena": "c",
      "buscar": "a",
      "insertar": "a"
    },
    {
      "inicio": "q1",
      "fin": "q1",
      "cadena": "b",
      "buscar": "b",
      "insertar": "x"
    },
    {
      "inicio": "q1",
      "fin": "q1",
      "cadena": "a",
      "buscar": "a",
      #esta aquí, o sea la transicion lambda que muestran en la diapositiva
      "insertar": "x"
    },
    {
      "inicio": "q1",
      "fin": "q2",
      #y aqui x2 :v
      "cadena": "x",
      "buscar": "#",
      "insertar": "#"
    }
  ]
}


