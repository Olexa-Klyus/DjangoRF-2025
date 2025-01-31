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
    advert_update: (id)=>`/auto/used/autos/${id}`,

    categories: '/auto/categories',
    marks: (id) => `/auto/categories/${id}/marks`,
    models: (id, pk) => `/auto/categories/${id}/marks/${pk}/models`,
    regions: '/auto/regions',
    cities: (id) => `/auto/regions/${id}/cities`,
    currency: `/auto/currency_points`,

    point_update: (ccy) => '/auto/currency_point_add/' + ccy,
}

export {
    baseURL,
    urls
}