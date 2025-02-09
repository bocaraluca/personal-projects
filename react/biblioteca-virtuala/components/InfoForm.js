import React from "react";
import { Box, Button, Paper, Typography } from "@mui/material";
import info from "./photos/info.jpeg";
import LoginForm from "./LoginForm";
import { Link } from "react-router-dom";
import { purple } from "@mui/material/colors";

const InfoForm = () => {
  return (
    <Paper
      elevation={4}
      sx={{
        width: "90vw",
        height: "700px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        alignSelf: "center",
        p: 2,
        gap: 1,
        borderRadius: "3px",
        backgroundImage: `url(${info})`,
        opacity: 0.67,
      }}
    >
      <Box
        sx={{
          marginY: "5px",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          borderRadius: "5px",
        }}
      >
        <Typography variant="h2" color={"white"}>
          Bine ați venit!
        </Typography>
        <Typography variant="h5" textAlign={"center"} color={"white"} marginTop={"40px"}>
          Înainte de a începe lectura, vă rugăm să vă autentificați pe contul dvs. de elev.
        </Typography>

        <LoginForm />

        <Typography color={"white"} fontSize={20}>
          Vă rugăm de asemenea să răspundeți la acest chestionar despre biblioteca
        </Typography>
        <Typography color={"white"} fontSize={20}>
          noastră virtuală pentru a ne ajuta să ne îmbunătățim serviciile.
        </Typography>
        <Link
          to={"/chestionar"}
          style={{ textTransform: "none", textDecoration: "none", color: "inherit" }}
        >
          <Button sx={{ bgcolor: purple[800], width: "250px", color: "white", marginTop: "20px", height: "50px" }}>Vezi chestionarul</Button>
        </Link>
      </Box>
    </Paper>
  );
};

export default InfoForm;