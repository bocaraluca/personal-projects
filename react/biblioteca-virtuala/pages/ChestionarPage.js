import { Box, Button, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import back from '../components/photos/back.jpg';
import React from 'react'
import IntrebareUnic from '../components/IntrebareUnic'
import IntrebareRaspuns from '../components/IntrebareRaspuns'
import IntrebareMultiple from '../components/IntrebareMultiple'

const ChestionarPage = () => {

  const handleSubmit = () => {
      alert("Răspunsurile au fost întregistrate cu succes. Vă mulțumim că ați completat chestionarul!");
  };

  return (
    <Box
      sx={{
        width: "100vw",
        height: "100%",
        backgroundImage: `url(${back})`,
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
        opacity: 0.95,
        display: "flex",
        flexDirection: "column",
        gap: 2,
        alignItems: 'center',
        paddingY: 5
      }}
    >
      <Typography fontSize={40}>Chestionar pentru elevi</Typography>

      <Box sx={{
        width: '90vw',
        height: '100%',
        border: '5px',
        borderColor: deepPurple[800],
        display: 'flex',
        flexDirection: 'column',
        gap: '30px'
      }}>
        <IntrebareRaspuns intrebare={"Numele și prenumele:"}/>
        <IntrebareRaspuns intrebare={"Liceul de proveniență:"}/>
        <IntrebareRaspuns intrebare={"Clasa:"}/>
        <IntrebareUnic intrebare={"Cât de des utilizați biblioteca virtuală?"} r1={"Zilnic"} r2={"Săptămânal"} 
          r3={"Lunar"} r4={"Niciodată"}/>
        <IntrebareMultiple intrebare={"Care sunt principalele motive pentru care utilizați această bibliotecă?"}
          r1={"Pentru ora de limba română"} r2={"În scop recreativ"} r3={"Pentru proiecte școlare"} r4={"Altele"}/>
        <IntrebareMultiple intrebare={"Care este genul vostru preferat de cărți?"}
          r1={"Acțiune și aventură"} r2={"Clasice"} r3={"Fantezie"} r4={"Romantism"}/>
        <IntrebareRaspuns intrebare={"Care este cartea voastră preferată de pe platformă?"}/>
        <IntrebareRaspuns intrebare={"Ce cărți credeți că ar trebui adăugate pe viitor în bibliotecă?"}/>
        <IntrebareUnic intrebare={"Ați recomanda această platformă colegilor/prietenilor?"} r1={"Cu siguranță"} r2={"Probabil că da"} 
          r3={"Nu sunt sigur/ă"} r4={"Nu"}/>

        <Button variant="contained" sx={{bgcolor: purple[800], width: '330px', height: '60px', alignSelf: 'center'}} onClick={handleSubmit}>Trimite răspunsurile</Button>
      </Box>  
    </Box>
  )
}

export default ChestionarPage