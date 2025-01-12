const baseURL = '/api'

const auth = '/auth'
const adverts = '/auto/search'

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