d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)

d.end()
