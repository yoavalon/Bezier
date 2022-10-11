d = DslBezier()

d.position_pen(1,0)
d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
