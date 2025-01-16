import {apiService, apiUserService} from "./apiService";
import {urls} from "../constants/urls";

const _accessTokenKey = 'access';
const _refreshTokenKey = 'refresh';

const authService = {
    async register(user) {
        const {data} = await apiUserService.post(urls.auth.register, user)
        return data
    },

    async activate(token) {
        const {data} = await apiUserService.patch(urls.auth.activate + token)
        return data;
    },

    async login(user) {
        const {data} = await apiUserService.post(urls.auth.login, user);
        this.setTokens(data);
        // const {data: me} = await this.me();
        // return me;
    },

    // me() {
    //     return apiService.get(urls.auth.me)
    // },

    setTokens({refresh, access}) {
        localStorage.setItem(_accessTokenKey, access);
        localStorage.setItem(_refreshTokenKey, refresh);
    },

    getAccessToken() {
        return localStorage.getItem(_accessTokenKey);

    },

    getRefreshToken() {
        return localStorage.getItem(_refreshTokenKey);
    },

    deleteTokens() {
        localStorage.removeItem(_accessTokenKey)
        localStorage.removeItem(_refreshTokenKey)
    },

    getSocketToken() {
        return apiService.get(urls.auth.socket)
    },

}

export {
    authService
}