const baseURL = '/api'

const register = '/users'
const auth = '/auth'
const adverts = '/auto/user/autos'
const activate = '/auth/activate/'

const urls = {
    auth: {
        register: register,
        activate: activate,
        login: auth,
        socket: `${auth}/socket`
    },
    adverts
}

export {
    baseURL,
    urls
}