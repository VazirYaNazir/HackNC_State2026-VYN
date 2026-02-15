import React from "react";
import { Button, Text, View } from "react-native";
import { useAuth } from "../auth/AuthContext";

export function SignInScreen() {
  const { signIn } = useAuth();

  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text style={{ marginBottom: 12 }}>You are logged out</Text>
      <Button title="Sign in" onPress={() => signIn("Parsa")} />
    </View>
  );
}
