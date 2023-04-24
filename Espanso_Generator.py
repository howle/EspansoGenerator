import time
import yaml

print("Examples of custom triggers:")
print(":omw: :brb: :ty: :shrug: :tableflip: :date: :time: :clip: :clipset: :up: :down: :rand:")

triggers = []

num_triggers = int(input("Enter the number of custom triggers: "))

for i in range(num_triggers):
    custom_trigger = input(f"Enter custom trigger {i+1}: ")

    replacement_parts = []
    vars_config = []
    while True:
        print("\nReplacement options:")
        print("1. Text")
        print("2. Shell command")
        print("3. Clipboard")
        print("4. Cursor movement")
        print("5. Finish")

        replacement_type = int(input("Choose the type of replacement (1-5): "))

        if replacement_type == 1:
            replacement_text = input("Enter replacement text: ")
            replacement_parts.append(replacement_text)
        elif replacement_type == 2:
            shell_command = input("Enter the shell command: ")
            replacement_parts.append("{{output}}")
            vars_config.append({"name": "output", "type": "shell", "params": {"cmd": shell_command}})
        elif replacement_type == 3:
            valid_replacements = ["$(clipboard)", "$(set-clipboard)"]
            for i in range(len(valid_replacements)):
                print(f"{i+1}. {valid_replacements[i]}")
            replacement_index = int(input("Enter the index of the desired replacement option: ")) - 1
            replacement = valid_replacements[replacement_index]
            replacement_parts.append(replacement)
        elif replacement_type == 4:
            valid_replacements = ["$(cursorUp)", "$(cursorDown)"]
            for i in range(len(valid_replacements)):
                print(f"{i+1}. {valid_replacements[i]}")
            replacement_index = int(input("Enter the index of the desired replacement option: ")) - 1
            replacement = valid_replacements[replacement_index]
            replacement_parts.append(replacement)
        elif replacement_type == 5:
            break

    triggers.append({"trigger": custom_trigger, "replace": "".join(replacement_parts), "vars": vars_config})

config = {"matches": triggers}
config_yaml = yaml.dump(config)

filename = f"{int(time.time())}.yaml"

with open(filename, "w") as f:
    f.write(config_yaml)
    print(f"Configuration saved to {filename}")

print("\nGenerated YAML configuration:\n")
print(config_yaml)
