d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.E, Orient.right, Length.short, Radius.low)
d.position_pen(2,3)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)

d.end()
