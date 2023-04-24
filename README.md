


# Espanso autokey builder.  This script allows users to define custom triggers and replacements, which can be used in applications that support trigger-based text replacement. The script outputs a YAML configuration file that can be used to configure the application. 

## Usage

1. Run the script in a Python environment:  python3 Espanso_Generator.py     

2. Follow the prompts to define the custom triggers and their corresponding replacements.

3. Once finished, the script will output the YAML configuration file.

4. Add the generated YAML configuration to your espanso base.yml file.

5. Restart espanso or reload the configuration.

6. Test the custom trigger to confirm it is working as expected.

## Example


```

python3 Espanso_Generator.py
Examples of custom triggers:
:omw: :brb: :ty: :shrug: :tableflip: :date: :time: :clip: :clipset: :up: :down: :rand:
Enter the number of custom triggers: 1
Enter custom trigger 1: HIYA

Replacement options:
1. Text
2. Shell command
3. Clipboard
4. Cursor movement
5. Finish
Choose the type of replacement (1-5): 1
Enter replacement text: Today is

Replacement options:
1. Text
2. Shell command
3. Clipboard
4. Cursor movement
5. Finish
Choose the type of replacement (1-5): 2
Enter the shell command: date

Replacement options:
1. Text
2. Shell command
3. Clipboard
4. Cursor movement
5. Finish
Choose the type of replacement (1-5): 5
Configuration saved to 1682139713.yaml

Generated YAML configuration:

matches:
- replace: Today is {{output}}
trigger: HIYA
vars:
- name: output
params:
cmd: date
type: shell
```



After adding the generated YAML configuration to your espanso base.yml file, the example trigger should work as expected. Typing in `HIYA`, in this example should convert to: `Today is Fri Apr 21 23:53:23 CDT 2023`. (or whatever the current date is) 





