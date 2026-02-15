import React from "react";
import { NavigationContainer, DefaultTheme } from "@react-navigation/native";
import { SafeAreaProvider } from "react-native-safe-area-context";

import { Colors } from "./src/theme/colors";
import { RootNavigator } from "./src/navigation/RootNavigator"; // adjust name if yours differs

const navTheme = {
  ...DefaultTheme,
  colors: {
    ...DefaultTheme.colors,
    background: Colors.black,
    card: Colors.black,       // header background
    text: Colors.white,
    border: Colors.gray500,
    primary: Colors.white,    // buttons/active tint default
    notification: Colors.gray200,
  },
};

export default function App() {
  return (
    <SafeAreaProvider>
      <NavigationContainer theme={navTheme}>
        <RootNavigator />
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
