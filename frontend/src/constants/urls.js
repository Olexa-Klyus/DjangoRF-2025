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


const privatBankAPI = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'


const options = {
    headers: {
        "Content-Type": "application/json",
        mode: "no-cors",
    }
}
const fetchHeaders = {

    // referer_policy: 'Access-Control-Allow-Origin',
    // content_type: "application/json",
    headers: {
        "Content-Type": "application/json"
    },
    mode: "no-cors",
}

export {
    baseURL,
    urls,
    privatBankAPI,
    fetchHeaders,
    options
}