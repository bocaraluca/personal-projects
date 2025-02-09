import { Box, Paper, Typography } from '@mui/material'
import React from 'react'
import eLibrary from "./photos/eLibrary.jpg"
import { purple } from '@mui/material/colors'

const AboutForm = () => {
  return (
    <Box sx={{
      width: "90vw",
      height: "90vh",
      display: "flex",
      flexDirection: "row",
      alignItems: "center",
      alignSelf: "center",
    }}>
    <Paper
        elevation={4}
        component="form"
        sx={{
            width: "1100px",
            height: "500px",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            alignSelf: "center",
            p: 2,
            gap: 1,
            borderRadius: "5px",
            backgroundImage: `url(${eLibrary})`,
            backgroundSize: 'cover',
            margin: '100px',
            marginRight: '150px'
        }}
    ></Paper>

    <Box sx={{
      width: "1000px",
      maxHeight: "500px",
      display: "flex",
      flexDirection: "column",
      backgroundColor: purple[800],
      padding: 5,
      borderRadius: '7px'
    }}>
      <Typography variant="h6" color={'white'}>Această bibliotecă virtuală este concepută special pentru a oferi elevilor o experiență educațională captivantă și accesibilă, 
care să îi încurajeze să exploreze lumea cărților și să își dezvolte pasiunea pentru învățare. Dispunem de o colecție de 20 de 
cărți care vă sunt accesibile doar printr-un simplu click. Nu mai este nevoie să purtați după voi cărțile fizice sau să mergeți 
la bibliotecă, deoarece toate resursele sunt disponibile online. Platforma este folositoare în special pentru elevii de clasa a XII-a,
întrucât conține majoritatea operelor care intră în programa pentru bacalaureat. Vă dorim o lectură plăcută!</Typography>
    </Box>

    </Box>
  )
}

export default AboutForm