import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/patulluiprocust.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const PatulLuiProcust = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Patul lui Procust</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Camil Petrescu</Typography>
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
                    backgroundSize: '320px'
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
            <Typography fontSize={'18px'} color={'white'}>"Patul lui Procust" este romanul unor vanități rănite: 
            a doamnei T. și a lui Fred Vasilescu, în primul rând. Tocmai ale celor cărora Autorul le dă cuvântul, 
            îi îndeamnă să scrie. Doamna T. reușește mai bine să se confeseze, deși nici ea până la capăt. Fred 
            Vasilescu, în schimb, nu vorbește deloc despre el însuși (nu aflăm niciodată de ce o părăsește pe doamna T., 
            pe care o iubea), preferând să se ocupe de Ladima și de Emilia, a căror relație îl intriga, fiindcă nu 
            descifrează în ea nicio urmă de vanitate. Din contra, o patimă greu stăpânită la Ladima, iar la Emilia 
            un vag dispreț de femeie nesatisfăcută de darurile preponderent epistolare ale poetului îndrăgostit.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://scorilos.files.wordpress.com/2012/08/camil-petrescu-patul-lui-procust.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default PatulLuiProcust