const baseURL = '/api'

const urls = {

    auth: {
        register: '/users',
        activate: '/auth/activate/',
        login: '/auth',
        socket: `auth/socket`
    },

    adverts: '/auto/user/autos',
    advert_info: (id) => '/auto/info/' + id,
}

export {
    baseURL,
    urls
}