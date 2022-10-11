d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.position_pen(1,1)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
