import Vue from 'vue'
import Vuex from 'vuex'
import $backend from './backend.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    cars: null,
    books: null,
    error: ''
  },
  mutations: { // must be synchronous
    SET_BOOKS: (state, books) => {
      state.books = books
    },
    CLEAR_BOOKS: (state) => {
      state.books = null
    },
    SET_CARS: (state, cars) => {
      state.cars = cars
    },
    SET_ERROR: (state, error) => {
      state.error = error
    }
  },
  actions: { // can be asynchronous
    setCars: (context) => {
      $backend.fetchCars()
        .then(response => context.commit('SET_CARS', response.data))
        .catch(error => context.commit('SET_ERROR', error))
    },
    setBooks: (context) => {
      $backend.fetchBooks()
        .then(response => context.commit('SET_BOOKS', response.data))
        .catch(error => context.commit('SET_ERROR', error))
    },
    clearBooks: (context) => {
      context.commit('CLEAR_BOOKS')
    }
  }
})
