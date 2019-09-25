#include <iostream>

void Jump()
{
    std::cout << "Jump" << std::endl;
}

void Fire()
{
    std::cout << "Fire" << std::endl;
}

// 接口类
class ICommand
{
public:
    ICommand() = default;
    virtual ~ICommand() = default;
    virtual void execute() = 0;
};

class JumpCommand : public ICommand
{
public:
    void execute()
    {
        Jump();
    }
};

class FireCommand : public ICommand
{
public:
    void execute()
    {
        Fire();
    }
};

class InputHander
{
public:
    void HandleInput();

    void BindKey();

private:
    ICommand *buttonX;
    ICommand *buttonY;
};

void InputHander::BindKey()
{
    buttonX = new JumpCommand();
    buttonY = new FireCommand();
}

void InputHander::HandleInput()
{
    char inputKey;
    std::cin >> inputKey;
    if (inputKey == 'x')
        buttonX->execute();
    else if (inputKey == 'y')
        buttonY->execute();
}

int main(int argc, char const *argv[])
{
    auto handler = new InputHander();
    handler->BindKey();
    while (true)
    {
        handler->HandleInput();
    }
    return 0;
}
