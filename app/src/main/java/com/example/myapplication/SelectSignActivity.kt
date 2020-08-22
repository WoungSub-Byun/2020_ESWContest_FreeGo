package com.example.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_selectsign.*

class SelectSignActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_selectsign)

        goSignIn.setOnClickListener{
            startActivity(Intent(this@SelectSignActivity,SignInActivity::class.java))
        }

        goSignUp.setOnClickListener {
            startActivity(Intent(this@SelectSignActivity, RegisterActivity::class.java))
        }
    }
}