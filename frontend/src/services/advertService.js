import {apiServiceAllowAny, apiService} from "./apiService";
import {urls} from "../constants/urls";
import {data} from "react-router-dom";

const advertService = {
    getAll() {
        return apiService.get(urls.adverts)
    },


    getById: async (id) => {
        const response = await apiService.get(urls.advert_info(+id));
        return response.data;
    },


    create: async (data) => {
        const response = await apiService.post(urls.auto_add, data)
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