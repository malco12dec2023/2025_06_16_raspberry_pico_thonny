//Final Step. Development Procedure
/*
Steps 1 - 3: Thonny IDE and Postman IDE
Steps 4 - 9: Android Studio IDE
*/

/*
4. Download the provided ZIP file, extract in a known location.
4.1. Open Android Studio IDE, go to File Menu >> Open and navigate to the location of the extracted file.
4.2. Wait for Sync to finish, then run AVD. Report encountered errors.
4.3. No error? Proceed to next steps.
*/

/*
5. Before <application> tag, add the following line of code in Android Manifest.xml
    <uses-permission android:name="android.permission.INTERNET"/>
*/

/*
6. After onCreate method of MainActivity.java, create the following user-define methods.

6.1. para sa widgets (components).
    void pinControl() {
        // wala muna laman
    }

6.2. para sa HTTP request (JSON).
    void sendJsonPostRequest() {
        // wala muna laman
    }

6.3. No error? Proceed to next steps.
*/

/*
// 7. Copy the contents of the user-define methods.
*/

/*
// 7.1. Copy the contents of the user-define methods for pinControl().
*/

    void pinControl() {
        ImageView iv_01_pin_on = findViewById(R.id.iv_01_pin_on);
        ImageView iv_02_pin_off = findViewById(R.id.iv_02_pin_off);

        iv_01_pin_on.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getBaseContext(), "Turning On...", Toast.LENGTH_SHORT).show();
                sendJsonPostRequest("On");
            }
        });

        iv_02_pin_off.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getBaseContext(), "Turning On...", Toast.LENGTH_SHORT).show();
                sendJsonPostRequest("Off");
            }
        });
    }

/*
// 7.2. Copy the contents of the user-define methods for sendJsonPostRequest().
7.2.1. Change the ip address to the IP of your Pico W.
*/

    private void sendJsonPostRequest(String s) {
        try {
            RequestQueue requestQueue = Volley.newRequestQueue(this);
            JSONObject jsonBody = new JSONObject();
            //{"ledInternal": 1, "ledExternal": 0,}
            jsonBody.put("led_internal_main", s);
            jsonBody.put("ledExternal", s);

            final String mRequestBody = jsonBody.toString();

            StringRequest stringRequest = new StringRequest(Request.Method.POST, "http://192.168.8.100/api/pagsend-ng-tatlong-data", new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    Log.i("MPM_LOG", response);
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    Log.e("LOG_RESPONSE", error.toString());
                }
            }) {
                @Override
                public String getBodyContentType() {
                    return "application/json; charset=utf-8";
                }

                @Override
                public byte[] getBody() throws AuthFailureError {
                    try {
                        return mRequestBody.getBytes("utf-8");
                    } catch (UnsupportedEncodingException uee) {
                        VolleyLog.wtf("Unsupported encoding while trying to get the bytes of %s using %s", mRequestBody, "utf-8");
                        return null;
                    }
                }

                @Override
                protected Response<String> parseNetworkResponse(NetworkResponse response) {
                    String responseString = "";
                    if (response != null) {
                        responseString = String.valueOf(response.statusCode);
                    }
                    return Response.success(responseString, HttpHeaderParser.parseCacheHeaders(response));
                }
            };
            requestQueue.add(stringRequest);
            // changing progress bar visibility on below line.
            // mpm_loading_progress_bar.setVisibility(View.GONE);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

/*
7.3. No error? Proceed to next steps.
*/

/*
8. Run AVD, click ON and OFF icon.
8.1. Observe Thonny Shell responses. No error? Proceed to next steps.
8.2. Modify the sendJsonPostRequest(String s) method to include the correct variable names used in python code.
8.2.1. Change jsonBody.put("led_internal_main", s); to >>
8.2.2. Change jsonBody.put("ledExternal", s); to >>
8.2.3. Add jsonBody.put("variable-name-na-nasa-python", s);

8.3. Run AVD, click ON and OFF icon, built-in LED must turn on and off.
*/
