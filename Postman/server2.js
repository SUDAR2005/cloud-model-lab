const express=require("express");
const bodyParser=require("body-parser");
const app=express();
app.use(bodyParser.json());

let datas=[
    {id:1,place:"salem",temp:'50c'},
    {id:2,place:"chennai",temp:"20c"},
    {id:3,place:"Madurai",temp:"35c"}
];

app.get('/weather',(req,res)=>{
    res.status(200).send(datas);
});

app.post('/weather',(req,res)=>{

    const newData={id:datas.length+1,place:req.body.place,temp:req.body.temp};
    datas.push(newData);
    res.status(201).json(newData);
    console.log("Successfully inserted data");
});

app.delete('/weather/:id',(req,res)=>{
    const data=datas.filter(p=>p.id!=parseInt(req.params.id));
    res.status(204).send();
    console.log("Deleted record successfully...");
});

app.put('/weather/:id',(req,res)=>{
    const data=datas.find(p=>p.id===parseInt(req.params.id));
    if(!temp) return res.status(404).send("post not found");

    temp.place=req.body.place;
    res.json(temp);
});

const port=5013;

app.listen(port,()=>{
    console.log("Connected to port.....");
});