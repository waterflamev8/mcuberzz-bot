const Eris = require('eris');
const config = require('./config.json')

const bot = new Eris(config.token, {
  intents: 4609
});

bot.on('ready', async () => {
  console.log('Ready!');

  await bot.editStatus('online', config.activity);
});

bot.on('error', (err) => {
  console.error(err);
});

bot.on('messageCreate', async (msg) => {
  if (!config.admins.includes(msg.author.id)) return;

  if (msg.content.startsWith(']echo ')) {
    await msg.delete();
    await msg.channel.createMessage(msg.content.slice(6));
  }

  if (msg.content.startsWith(']embed ')) {
    await msg.delete();
    await msg.channel.createMessage({
      embed: {
        description: msg.content.slice(6),
        color: 0x0074ff
      }
    });
  }
});

bot.connect();
