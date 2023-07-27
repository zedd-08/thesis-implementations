import os, sys
os.environ["BING_U_COOKIE"] = "1Kzcptqy6FNqT8nKCd4XJjpN2Cz3TTfev0i0svUgGF2joQXu7OFHPVBXw1wrHxNdkH25V3prph2zoxOkM_RJheN2-DjnSLB93E5s2u3tnVH2Vrztz_wcolZbE0omGmViPDnClY-41Q9mJEPkPp_YJskLNE-FCsxsA0hX8V3GmHgLbtpM_RfIVIYuyB2TK9RuJnyBTrBZeKriOTn4d_OgcKQ"

data_dir = "../../../data"

import asyncio

from sydney import SydneyClient

async def main() -> None:
    async with SydneyClient() as sydney:
        while True:
            prompt = input("You: ")

            if prompt == "!reset":
                await sydney.reset_conversation()
                continue
            elif prompt == "!exit":
                break

            prompt = doc + prompt

            print("Sydney: ", end="", flush=True)
            async for response in sydney.ask_stream(prompt):
                print(response, end="", flush=True)
            print("\n")


if __name__ == "__main__":
    with open(os.path.join(data_dir, sys.argv[1])) as f:
        doc = f.read()
    doc += "\n"
    asyncio.run(main())