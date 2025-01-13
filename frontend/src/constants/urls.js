const baseURL = '/api'

const auth = '/auth'
const adverts = '/auto/user/autos'

const urls = {
    auth: {
        login: auth,
        socket: `${auth}/socket`
    },
    adverts
}

export {
    baseURL,
    urls
}