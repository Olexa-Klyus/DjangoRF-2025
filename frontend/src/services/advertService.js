import {apiAllowAnyService, apiService} from "./apiService";
import {urls} from "../constants/urls";

const advertService = {
    getAll() {
        return apiService.get(urls.adverts)
    },


    getById: async (id) => {
        const response = await apiAllowAnyService.get(urls.advert_info(+id));
        return response.data;
    },


    create(data) {
        return apiService.post(urls.adverts, data)
    }
}

export {
    advertService
}