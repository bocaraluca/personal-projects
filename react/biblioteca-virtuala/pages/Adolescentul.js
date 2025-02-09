import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/adolescentul.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const Adolescentul = () => {
  return (
    <Box sx={{
        width: "100vw",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        alignSelf: "center",
        //gap: 1,
        borderRadius: "2px",
        backgroundImage: `url(${back})`,
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
        opacity: 0.95
      }}>
        <Typography fontSize={60} paddingTop={'5px'}>Adolescentul</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de F.M. Dostoievski</Typography>
        <Box sx={{
            width: "90vw",
            height: "90vh",
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
            alignSelf: "center",
            }}>
            <Paper
                elevation={7}
                component="form"
                sx={{
                    width: '370px',
                    height: '440px',
                    alignSelf: "center",
                    p: 2,
                    gap: 1,
                    borderRadius: "5px",
                    backgroundImage: `url(${poza})`,
                    margin: '70px',
                    marginRight: '150px',
                    backgroundRepeat: 'no-repeat',
                    backgroundSize: 'cover'
                }}
            ></Paper>

            <Box sx={{
            width: "1000px",
            maxHeight: "300px",
            display: "flex",
            flexDirection: "column",
            backgroundColor: purple[800],
            padding: '35px',
            borderRadius: '7px'
            }}>
            <Typography fontSize={'18px'} color={'white'}>"Adolescentul", publicat inițial în 1875, este un roman profund al lui 
            Fyodor Dostoievski care explorează etapele formative ale tânărului Arkadi Dolgoruky în căutarea identității sale
            și a sensului vieții. Pe măsură ce călătorește spre Sankt Petersburg pentru a se apropia de tatăl său biologic, 
            Arkadi este martor la lumea complexă și adesea necruțătoare a adulților. Această experiență inițiatică îi schimbă 
            profund percepția asupra lumii și îl conduce către o înțelegere mai profundă a propriei sale ființe și a dilemelor 
            morale cu care se confruntă. Prin personajul Arkadi, Dostoevski adâncește în întrebări esențiale despre viață, 
            destin și sensul existenței umane, oferind cititorului o incursiune fascinantă în labirintul complex al psihicului 
            uman.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://gawrylyta.wordpress.com/wp-content/uploads/2011/10/feodor-mihailovici-dostoievski-adolescentul.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default Adolescentul