import React from "react";
import { Text, View } from "react-native";
import { Screen } from "../components/Screen";
import { Colors } from "../theme/colors";

export function HomeScreen() {
  return (
    <Screen>
      <View style={{ padding: 16 }}>
        <Text style={{ color: AppColors.text, fontSize: 22 }}>Home</Text>
        <Text style={{ color: AppColors.mutedText, marginTop: 8 }}>
          Using the palette everywhere.
        </Text>
      </View>
    </Screen>
  );
}
