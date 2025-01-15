const baseURL = '/api'

const register = '/users'
const auth = '/auth'
const adverts = '/auto/user/autos'

const urls = {
    auth: {
        register: register,
        login: auth,
        socket: `${auth}/socket`
    },
    adverts
}

export {
    baseURL,
    urls
}