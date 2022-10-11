d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.W, Length.medium)

d.end()
