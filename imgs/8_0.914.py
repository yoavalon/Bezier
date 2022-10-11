d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)

d.end()
