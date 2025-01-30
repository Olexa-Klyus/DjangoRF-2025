import {apiServiceAllowAny} from "./apiService";
import {urls} from "../constants/urls";

const categoryService = {
    getAll: async () => {
        const response = await apiServiceAllowAny.get(urls.categories)
        return response.data;
    }
}
const markService = {
    getById: async (id) => {
        const response = await apiServiceAllowAny.get(urls.marks(+id))
        return response.data;
    }
}
const modelService = {
    getById: async (id, pk) => {
        const response = await apiServiceAllowAny.get(urls.models(+id, +pk))
        return response.data;
    }
}
const regionService = {
    getAll: async () => {
        const response = await apiServiceAllowAny.get(urls.regions)
        return response.data;
    }
}

export {
    categoryService, markService, modelService,regionService
}