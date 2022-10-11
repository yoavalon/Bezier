d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)

d.end()
