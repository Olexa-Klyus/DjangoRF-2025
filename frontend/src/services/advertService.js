import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const advertService = {
    getAll: async () => {
        const response = await apiService.get(urls.adverts)
        console.log(response.data)
        return response.data;
    },

    // getById: async (id) => {
    //     const response = await apiService.get(urls.advert(+id));
    //     return response.data;
    // },

    getInfo: async (id) => {
        const response = await apiService.get(urls.advert_info(+id));
        return response.data;
    },

    create: async (data) => {
        const response = await apiService.post(urls.auto_add, data)
        return response.data
    },

    update: async (id, data) => {
        const response = await apiService.patch(urls.advert_update(+id), data)
        return response.data
    },

    updatePoint: async (ccy, data) => {
        const response = await apiService.patch(urls.point_update(ccy), data)
        return response.data
    }

}

export {
    advertService
}