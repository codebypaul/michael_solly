const express = require('express')
const app = express()
const layouts = require('express-ejs-layouts')
const PORT = process.env.PORT || 8000

app.set('view engine','ejs')
app.use(layouts)

app.get('/',(req,res)=>{
    res.render('home')
})

app.use(express.static(__dirname+'/public'))

app.listen(PORT,()=>{
    console.log(`connected to PORT:${PORT}`);
    console.log('you will buy a car...');
})