import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchResource () {
    return $axios.get(`resource/q`)
      .then(response => response.data)
  },

  fetchSecureResource () {
    return $axios.get(`secure-resource/xxx`)
      .then(response => response.data)
  },

  fetchResourceTest () {
    return $axios.get(`test`)
      .then(response => response.data)
  },

  fetchBooks () {
    return $axios.get(`books`)
      .then(response => response.data)
  },

  fetchCars () {
    return $axios.get(`vega_cars`)
      .then(response => response)
  }
}
