package com.example.myapplication

import android.content.Intent
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView


class GuideFragment3 : Fragment() {

    private lateinit var guide3Image1 : ImageView
    private lateinit var guide3Button : Button
    private lateinit var guide3Text : TextView

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_guide3, container, false)
        // Inflate the layout for this fragment
        guide3Image1 = view.findViewById(R.id.guide3Image1)
        guide3Button = view.findViewById(R.id.guide3Button)
        guide3Text = view.findViewById(R.id.guide3Text)

        guide3Image1.animate().alpha(1f).setDuration(1000).start()
        guide3Button.animate().alpha(1f).setDuration(1000).withEndAction {
            guide3Text.animate().alpha(1f).setDuration(1000).start()
        }.start()

        guide3Button.setOnClickListener {
            startActivity(Intent(context,FridgeActivity::class.java))
            activity?.finish()
        }

        return view
    }


}