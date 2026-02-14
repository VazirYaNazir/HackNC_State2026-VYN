import { Image, StyleSheet, Text, View } from "react-native";
import { Screen } from "./src/components/Screen";

const styles = StyleSheet.create({
  title: {
    color: "white",
    marginTop: 60,
    marginLeft: 20,
    fontSize: 24,
  },
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  image: {
    width: 200,
    height: 200,
  },
});

export default function App() {
  return (
    <Screen backgroundColor="#111827">
      <Text style={styles.title}>Hello</Text>

      <View style={styles.container}>
        <Image
          source={require("./assets/cortisol.png")}
          style={styles.image}
          resizeMode="contain"
        />
      </View>
    </Screen>
  );
}

