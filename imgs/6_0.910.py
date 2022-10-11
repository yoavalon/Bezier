d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)

d.end()
