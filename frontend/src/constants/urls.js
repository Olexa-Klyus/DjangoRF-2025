const baseURL = '/api'

const urls = {

    auth: {
        register: '/users',
        activate: '/auth/activate/',
        login: '/auth',
        socket: `auth/socket`
    },
    adverts: '/auto/user/autos',
    advert_info: (id) => `/auto/info/${id}`,
    auto_add: '/auto/used/autos',

    categories: '/auto/categories',
    brands: (id) => `/auto/categories/${id}/marks`,

    point_update: (ccy) => '/auto/currency_point_add/' + ccy,
}

export {
    baseURL,
    urls
}