import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/crimasipedeapsa.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const CrimaSiPedeapsa = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Crimă și pedeapsă</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>„O ființă superioară are oare dreptul să săvârșească o crimă 
            dacă aceasta este în folosul întregii umanități?” – iată întrebarea care îl macină necontenit pe Raskolnikov, 
            un fost student idealist, excentric și mizantrop, in ceasurile lungi de meditație din odaia sa strâmtă de 
            la mansardă. Sub presiunea sărăciei cumplite, a însingurării și a sentimentului de zădărnicie a tuturor 
            aspirațiilor sale, această teorie îndrăzneață este pusă peste noapte în aplicare, ducând la un asasinat 
            de o sălbăticie care zguduie întreg orașul Sankt Petersburg. Dostoievski analizează cu intuiția unui fin 
            psiholog cauzele crimei, dilemele personajului sau, pendulările sale lăuntrice între bine și rău, rațional 
            și irațional, psihologia ucigașului și a anchetatorului, avansând in final posibilitatea mântuirii prin 
            iubire, umilință si jertfa de sine.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://gawrylyta.wordpress.com/wp-content/uploads/2011/10/dostoievski-crima-si-pedeapsa.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default CrimaSiPedeapsa