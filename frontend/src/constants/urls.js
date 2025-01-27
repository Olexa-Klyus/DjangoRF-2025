const baseURL = '/api'

const urls = {

    auth: {
        register: '/users',
        activate: '/auth/activate/',
        login: '/auth',
        socket: `auth/socket`
    },
    categories:'/auto/categories',
    auto_add: '/auto/used/autos',
    adverts: '/auto/user/autos',
    advert_info: (id) => '/auto/info/' + id,
    point_update: (ccy) => '/auto/currency_point_add/' + ccy,
}

export {
    baseURL,
    urls
}