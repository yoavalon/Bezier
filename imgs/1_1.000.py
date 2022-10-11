d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(2,0)

d.end()
