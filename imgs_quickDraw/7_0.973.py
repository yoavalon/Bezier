d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.position_pen(3,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
