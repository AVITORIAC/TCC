import { create } from "zustand"

export const useStore = create((set) => ({
    url: 'http://127.0.0.1:8000/api/v1', // variavel
    setUrl: (newValue) => set({url: newValue}), // variavel de edição

    id: 0,
    setId: (newValue) => set({id: newValue}),

    token: '',
    setToken: (newValue) => set({token: newValue}),

    cargo: '',
    setCargo: (newValue) => set({cargo: newValue}),

    curso: '',
    setCurso: (newValue) => set({curso: newValue}),

    cargoCadastro: '',
    setCargoCadastro: (newValue) => set({cargoCadastro: newValue}),
}))