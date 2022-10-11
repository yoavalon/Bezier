d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)

d.end()
