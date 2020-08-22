package com.example.myapplication.retrofit.API

import com.example.myapplication.retrofit.DTO.BarCodeFoodInfo
import com.example.myapplication.retrofit.DTO.FirstData
import com.example.myapplication.retrofit.DTO.FoodData
import retrofit2.Call
import retrofit2.http.*

interface FridgeAPI {
    @GET("/show/{id}")
    fun getTable(
        @Path("id") id: String
    ) : Call<FoodData>

    @POST("/find/{id}")
    fun findFood(
        @Path("id") id : String,
        @Query("p_name") p_name : String
    ) : Call<FirstData>

    @POST("late/{id}")
    fun findLateFood(
        @Path("id") id : String
    ) : Call<FoodData>

    @POST("/insert")
    fun insertFood(
        @Field("id") id : String,
        @Field("p_name") p_name: String,
        @Field("p_number") p_number : Int,
        @Field("p_ex_date") p_ex_date : String
    ) : Call<FirstData>

    @PUT("/update")
    fun updateFood(
        @Field("id") id : String,
        @Field("p_name") p_name: String,
        @Field("p_number") p_number: Int
    ) : Call<FirstData>

    @DELETE("/delete")
    fun deleteFood(
        @Field("id") id : String,
        @Field("p_name") p_name: String
    ) : Call<FirstData>

    @GET("/lookupcode/{code}")
    fun barCodeShow(
        @Path("code") code : String
    ) : Call<BarCodeFoodInfo>

}