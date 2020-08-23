package com.example.myapplication

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import com.example.myapplication.retrofit.API.RetrofitHelper
import com.example.myapplication.retrofit.DTO.FirstData
import kotlinx.android.synthetic.main.activity_signin.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class SignInActivity : AppCompatActivity() {

    val service = RetrofitHelper().getUserAPI()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_signin)

        getData()

//        if(IDText.text.toString().isNotEmpty() && PwdText.text.toString().isNotEmpty()){
//            service.getUser(IDText.text.toString()).enqueue(object : Callback<FirstData>{
//                override fun onFailure(call: Call<FirstData>, t: Throwable) {
//                    Log.d("LOGIN", t.toString())
//                    Toast.makeText(this@SignInActivity, "로그인 중 오류발생", Toast.LENGTH_LONG).show()
//                }
//
//                override fun onResponse(call: Call<FirstData>, response: Response<FirstData>) {
//                    if(response.isSuccessful){
//                        if(response.body() != null){
//                            if(response.body()!!.code == 200){
//                                val intent = Intent(this@SignInActivity, FridgeActivity::class.java)
//                                intent.putExtra("name",IDText.text.toString())
//                                startActivity(intent)
//                            } else {
//                                IDText.text = null
//                                PwdText.text = null
//                            }
//                        }
//                    }
//                }
//            })
//        }

        btnSignIn.setOnClickListener {
            if(IDText.text.toString().isNotEmpty() && PwdText.text.toString().isNotEmpty()){
                service.login(IDText.text.toString(), PwdText.text.toString()).enqueue(object : Callback<FirstData>{
                    override fun onFailure(call: Call<FirstData>, t: Throwable) {
                        Log.d("LOGIN", t.toString())
                        Toast.makeText(this@SignInActivity, "로그인 중 오류발생", Toast.LENGTH_LONG).show()
                    }

                    override fun onResponse(call: Call<FirstData>, response: Response<FirstData>) {
                        if(response.isSuccessful){
                            if(response.body() != null){
                                if(response.body()!!.code == 200){
                                    val intent = Intent(this@SignInActivity, WelcomeActivity::class.java)
                                    intent.putExtra("name",IDText.text.toString())
                                    saveData()
                                    startActivity(intent)
                                }
                            }
                        }
                    }
                })
            }
        }
    }

    fun saveData(){
        val pref = this.getSharedPreferences("user", Activity.MODE_PRIVATE)
        val editor = pref.edit()
        editor.putString("ID",IDText.text.toString())
        editor.putString("PWD", PwdText.text.toString())
        editor.apply()
    }

    private fun getData(){
        val pref = this.getSharedPreferences("user", Activity.MODE_PRIVATE)
        val id = pref.getString("ID","")
        val pwd = pref.getString("PWD", "")
        IDText.setText(id)
        PwdText.setText(pwd)
    }
}